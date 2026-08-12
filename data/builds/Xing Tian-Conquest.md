---
type: smite-build
god: Xing Tian
mode: Conquest
builds:
- source: community
  aspect: Aspect of Relentless Spite
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.67
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.58
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.53
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.51
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.59
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.57
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.56
  - name: Dwarven Plate
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.46
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.63
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.71
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.43
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.57
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.41
    win_rate: 0.53
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.62
  - name: War Flag
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/xing-tian/
  last_verified: '2026-08-11'
  god_win_rate: 0.5624729788153913
  god_matches_won: 1301
  god_matches_played: 2313
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Draconic
    Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide, Stone of
    Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s Shield,
    Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.4
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s Grace,
    Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Spectral Armor, Leviathan''s
    Hide, Blood-Bound Book, Lifebinder, Bancroft''s Talon, Midgardian Mail, Glorious
    Pridwen, Gladiator''s Shield, Ancile, Jade Scepter, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.36
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.92
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.4
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita Charm, Stone
    of Binding, Spear of the Magus, Freya''s Tears, Screeching Gargoyle, Void Shield,
    The Cosmic Horror, Oni Hunter''s Garb, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Erosion, Obsidian Shard, Eye of Providence, Spectral Armor, Draconic
    Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian Mail,
    The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.27
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.66
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.4
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Freya''s Tears,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion,
    Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic Scale, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Mantle Of Discord, Stone of Binding, Spear
    of the Magus, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp, Bancroft''s Talon,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.2
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.47
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb,
    Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak,
    Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.58
      pick: 0.4
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Soul Gem, Hydra''s Lament,
    Freya''s Tears, Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion,
    Spectral Armor, Death Metal, Spear of the Magus, Eye of Providence, Shogun''s
    Ofuda, The Reaper, Draconic Scale, Damaru, The Cosmic Horror, Avenging Blade,
    Helm of Radiance, Riptalon, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Silverbranch Bow, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Freya''s
    Tears, Spear of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, The
    Cosmic Horror, Runeforged Hammer, Shield Splitter, Helm of Radiance, Shield of
    the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of the Storm, Rod
    of Asclepius, Eye of Providence, Pharaoh''s Curse, Obsidian Shard, Jade Scepter,
    Draconic Scale, Chronos'' Pendant, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.23
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.52
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence,
    Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.52
      win: 0.58
      pick: 0.4
      fit: 0.71
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.71
  starter: *id001
---
