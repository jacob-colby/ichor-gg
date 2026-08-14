---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.14
    win_rate: 0.88
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.6
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.57
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.31
  - name: Stampede
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.8
    - name: Shogun's Ofuda
      pick_rate: 0.07
      win_rate: 0.38
  - name: Kinetic Cuirass
    pick_rate: 0.08
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.63
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.83
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.5
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.4
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.67
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.33
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.18
    win_rate: 0.71
  - name: Sundering Axe
    pick_rate: 0.11
    win_rate: 0.77
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-14'
  god_win_rate: 0.5042735042735043
  god_matches_won: 59
  god_matches_played: 117
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
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
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye
    of Providence, Draconic Scale, Spectral Armor, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Soul Gem, Magi''s Cloak,
    Ancile, Gladiator''s Shield, Xibalban Effigy, Prophetic Cloak, Hide of the Nemean
    Lion, Void Shield, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.82
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.16
      fit: 0.72
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Gluttonous Grimoire,
    Soul Gem, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s Grace,
    Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Phoenix Feather,
    Spectral Armor, Leviathan''s Hide, Blood-Bound Book, Lifebinder, Midgardian Mail,
    Bancroft''s Talon, Glorious Pridwen, Gladiator''s Shield, Ancile, Hide of the
    Nemean Lion, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.35
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.16
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Spear of the Magus
  flex_slots:
  - Stone of Binding
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Gluttonous Grimoire, Soul Gem, Amanita Charm, Stone
    of Binding, Spear of the Magus, Screeching Gargoyle, Breastplate of Valor, Freya''s
    Tears, Void Shield, Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Shield
    of the Phoenix, Spear of Desolation, Erosion, Obsidian Shard, Eye of Providence,
    Spectral Armor, Draconic Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of
    Discord, Midgardian Mail, The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.58
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.16
      fit: 0.48
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.4
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Gluttonous Grimoire, Amanita Charm, Breastplate of
    Valor, Freya''s Tears, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral
    Armor, Erosion, Eye of Providence, Bracer of The Abyss, Draconic Scale, Helm of
    Radiance, Leviathan''s Hide, Death Metal, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Yogi''s Necklace, Bragi''s Harp, Rod of Asclepius, Blood-Bound
    Book, Bancroft''s Talon, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.2
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.48
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
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
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Breastplate of Valor,
    Freya''s Tears, Shield of the Phoenix, Amanita Charm, Soul Gem, Gluttonous Grimoire,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Chandra''s Grace,
    Gladiator''s Shield, Erosion, Spectral Armor, Spear of Desolation, Prophetic Cloak,
    Eye of Providence, Draconic Scale, Helm of Radiance, Gem of Focus, Totem of Death,
    Leviathan''s Hide, Mantle Of Discord, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.57
      pick: 0.16
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Runeforged Hammer, Kinetic Cuirass, Jotunn''s
    Revenge, Gluttonous Grimoire, The Crusher, Amanita Charm, Breastplate of Valor,
    Soul Gem, Hydra''s Lament, Freya''s Tears, Oni Hunter''s Garb, Shield Splitter,
    Pharaoh''s Curse, Golden Blade, Lernaean Bow, Shield of the Phoenix, Eye of the
    Storm, Erosion, Spectral Armor, Death Metal, Spear of the Magus, Eye of Providence,
    Damaru, Draconic Scale, The Reaper, The Cosmic Horror, Avenging Blade, Helm of
    Radiance, Riptalon, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Stone
    of Binding, Heartseeker, Silverbranch Bow, Yogi''s Necklace, Tekko-Kagi, Shogun''s
    Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.52
    Runeforged Hammer:
      total: 0.66
      efficiency: 0.55
      win: 0.88
      pick: 0.14
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Genji's Guard
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Runeforged Hammer, Kinetic Cuirass,
    Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Amanita Charm, Soul Gem,
    Breastplate of Valor, Freya''s Tears, Spear of the Magus, Oni Hunter''s Garb,
    Hydra''s Lament, Death Metal, The Cosmic Horror, Helm of Radiance, Shield Splitter,
    Shield of the Phoenix, Pharaoh''s Curse, Spectral Armor, Erosion, Spear of Desolation,
    Rod of Asclepius, Eye of the Storm, Eye of Providence, Jade Scepter, Obsidian
    Shard, Golden Blade, Lernaean Bow, Draconic Scale, Chronos'' Pendant, Leviathan''s
    Hide, Blood-Bound Book, Damaru, Bancroft''s Talon, Bracer of The Abyss, The Reaper,
    Midgardian Mail, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.5
    Runeforged Hammer:
      total: 0.65
      efficiency: 0.55
      win: 0.88
      pick: 0.14
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.42
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
  - Shifter's Shield
  - Breastplate of Valor
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
    Grimoire, Breastplate of Valor, Erosion, Oni Hunter''s Garb, Shield of the Phoenix,
    Eye of Providence, Draconic Scale, Spectral Armor, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Soul Gem, Magi''s Cloak,
    Ancile, Gladiator''s Shield, Xibalban Effigy, Prophetic Cloak, Hide of the Nemean
    Lion, Void Shield, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.48
      pick: 0.25
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.56
      pick: 0.13
      fit: 0.82
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.55
      efficiency: 0.52
      win: 0.57
      pick: 0.16
      fit: 0.72
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
---
