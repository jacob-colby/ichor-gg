---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.48
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.26
    win_rate: 0.52
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.51
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.49
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.43
    alternates:
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.46
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.63
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.64
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.63
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.56
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.47
  community_starters:
  - name: Selflessness
    pick_rate: 0.42
    win_rate: 0.45
  - name: Heroism
    pick_rate: 0.25
    win_rate: 0.58
  - name: Conduit Gem
    pick_rate: 0.06
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-08-10'
  god_win_rate: 0.5088
  god_matches_won: 318
  god_matches_played: 625
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
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
  - Amanita Charm
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Shield of the Phoenix, Shifter''s Shield, Erosion, Oni Hunter''s Garb, Eye of
    Providence, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide, Mantle
    Of Discord, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak,
    Gladiator''s Shield, Screeching Gargoyle, Ancile, Xibalban Effigy, Void Shield,
    Hide of the Nemean Lion, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.7
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Chandra''s Grace, Oni Hunter''s
    Garb, Shifter''s Shield, Erosion, Eye of Providence, Draconic Scale, Phoenix Feather,
    Spectral Armor, Blood-Bound Book, Leviathan''s Hide, Bancroft''s Talon, Lifebinder,
    Midgardian Mail, Glorious Pridwen, Gladiator''s Shield, Ancile, Helm of Radiance,
    Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.37
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.58
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Stone of Binding, Screeching Gargoyle, Spear of the Magus, Void
    Shield, Oni Hunter''s Garb, The Cosmic Horror, Shield of the Phoenix, Spear of
    Desolation, Void Stone, Shifter''s Shield, Erosion, Eye of Providence, Obsidian
    Shard, Spectral Armor, Draconic Scale, Leviathan''s Hide, Helm of Radiance, Mantle
    Of Discord, Midgardian Mail, Doom Orb.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.28
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Shifter''s
    Shield, Erosion, Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic
    Scale, Death Metal, Leviathan''s Hide, Midgardian Mail, Yogi''s Necklace, Mantle
    Of Discord, Spear of the Magus, Stone of Binding, Rod of Asclepius, Bragi''s Harp,
    Blood-Bound Book, Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.21
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.21
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb,
    Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation, Chandra''s Grace,
    Gladiator''s Shield, Shifter''s Shield, Erosion, Spectral Armor, Eye of Providence,
    Draconic Scale, Helm of Radiance, Prophetic Cloak, Gem of Focus, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Mantle Of Discord, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.48
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Oni Hunter's Garb:
      total: 0.49
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Gluttonous Grimoire
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Hydra''s
    Lament, Soul Gem, Runeforged Hammer, Oni Hunter''s Garb, Shield Splitter, Pharaoh''s
    Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Death
    Metal, Shifter''s Shield, Erosion, Spectral Armor, Spear of the Magus, Eye of
    Providence, Damaru, The Reaper, Shogun''s Ofuda, Draconic Scale, Avenging Blade,
    The Cosmic Horror, Helm of Radiance, Leviathan''s Hide, Riptalon, Midgardian Mail,
    Mantle Of Discord, Stone of Binding, Heartseeker, Spear of Desolation, Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s
    Shield, Spear of the Magus, Oni Hunter''s Garb, Death Metal, Hydra''s Lament,
    Runeforged Hammer, The Cosmic Horror, Shield Splitter, Shield of the Phoenix,
    Helm of Radiance, Spear of Desolation, Shifter''s Shield, Erosion, Eye of the
    Storm, Spectral Armor, Rod of Asclepius, Eye of Providence, Pharaoh''s Curse,
    Jade Scepter, Obsidian Shard, Draconic Scale, Chronos'' Pendant, Golden Blade,
    Damaru, Leviathan''s Hide, Lernaean Bow, The Reaper, Blood-Bound Book, Bancroft''s
    Talon, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.24
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.24
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.54
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
    Grimoire, Shield of the Phoenix, Shifter''s Shield, Erosion, Oni Hunter''s Garb,
    Eye of Providence, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide,
    Mantle Of Discord, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s
    Cloak, Gladiator''s Shield, Prophetic Cloak, Screeching Gargoyle, Ancile, Xibalban
    Effigy, Void Shield, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.53
      pick: 0.27
      fit: 0.4
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.19
      fit: 0.4
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.63
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.7
  starter: *id001
---
