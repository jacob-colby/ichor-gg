---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.4
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.51
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.46
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.61
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.51
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.52
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.47
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.7
  - name: Dwarven Plate
    pick_rate: 0.07
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.65
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.48
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.41
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.67
    - name: Medallion
      pick_rate: 0.05
      win_rate: 0.55
  community_starters:
  - name: Selflessness
    pick_rate: 0.23
    win_rate: 0.52
  - name: War Flag
    pick_rate: 0.15
    win_rate: 0.45
  - name: Warrior's Axe
    pick_rate: 0.14
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-10'
  god_win_rate: 0.5264227642276422
  god_matches_won: 259
  god_matches_played: 492
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
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Gluttonous Grimoire, Shield of the Phoenix, Oni Hunter''s Garb, Erosion, Eye of
    Providence, Draconic Scale, Jotunn''s Revenge, Spectral Armor, Pharaoh''s Curse,
    Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone of Binding,
    The Crusher, Midgardian Mail, Eye of the Storm, Hydra''s Lament, Shogun''s Ofuda,
    Helm of Radiance, Magi''s Cloak, Runeforged Hammer, Gladiator''s Shield, Screeching
    Gargoyle, Ancile, Prophetic Cloak, Xibalban Effigy, Void Shield, Doublet of Binding,
    Rod of Asclepius, Yogi''s Necklace, Hussar''s Wings, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.55
      pick: 0.25
      fit: 0.38
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.38
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.12
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Rod of Asclepius, Chandra''s
    Grace, Oni Hunter''s Garb, Erosion, Eye of Providence, Phoenix Feather, Draconic
    Scale, Jotunn''s Revenge, Spectral Armor, Pharaoh''s Curse, Leviathan''s Hide,
    Blood-Bound Book, Bancroft''s Talon, Midgardian Mail, Glorious Pridwen, Runeforged
    Hammer, Lifebinder, The Crusher, Eye of the Storm, Shogun''s Ofuda, Shield Splitter,
    Riptalon, Hydra''s Lament, Gladiator''s Shield, Ancile, The Reaper, Yogi''s Necklace,
    Void Shield, Mantle Of Discord, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.55
      pick: 0.25
      fit: 0.35
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.12
      fit: 0.55
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Jotunn''s Revenge, Kinetic
    Cuirass, Soul Gem, The Crusher, Amanita Charm, Berserker''s Shield, Stone of Binding,
    Screeching Gargoyle, Spear of the Magus, Void Shield, Oni Hunter''s Garb, The
    Cosmic Horror, Shield of the Phoenix, Void Stone, Spear of Desolation, Avenging
    Blade, Erosion, Eye of Providence, Spectral Armor, Obsidian Shard, Riptalon, Pharaoh''s
    Curse, Draconic Scale, Silverbranch Bow, Hydra''s Lament, The Reaper, Shield Splitter,
    Leviathan''s Hide, Mantle Of Discord, Runeforged Hammer, Helm of Radiance, Midgardian
    Mail, Shogun''s Ofuda, Heartseeker, Eye of the Storm.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.25
      fit: 0.27
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.12
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Gluttonous Grimoire
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Golden Blade, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, The
    Crusher, Oni Hunter''s Garb, Soul Gem, Lernaean Bow, Shogun''s Ofuda, Shield of
    the Phoenix, Hydra''s Lament, Silverbranch Bow, Tyrfing, Runeforged Hammer, Spectral
    Armor, Erosion, Shield Splitter, Eye of Providence, Bracer of The Abyss, Draconic
    Scale, Eye of the Storm, Helm of Radiance, Leviathan''s Hide, Midgardian Mail,
    Yogi''s Necklace, Mantle Of Discord, Death Metal, Stone of Binding, Eros'' Bow,
    Dominance, Spear of the Magus, Rod of Asclepius.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.55
      pick: 0.25
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.12
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.33
    Pharaoh's Curse:
      total: 0.5
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire,
    Berserker''s Shield, Hydra''s Lament, Oni Hunter''s Garb, Screeching Gargoyle,
    Chronos'' Pendant, The Crusher, Spear of Desolation, Chandra''s Grace, Gladiator''s
    Shield, Erosion, Spectral Armor, Eye of Providence, Prophetic Cloak, Pharaoh''s
    Curse, Shield Splitter, Draconic Scale, Runeforged Hammer, Helm of Radiance, Gem
    of Focus, Leviathan''s Hide, Eye of the Storm, Mantle Of Discord, Midgardian Mail,
    Rod of Asclepius, Stone of Binding, Spear of the Magus, Death Metal, Arondight,
    Jade Scepter, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.55
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.12
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Freya''s Tears, Gluttonous Grimoire, Shield of the Phoenix, Oni Hunter''s Garb,
    Erosion, Eye of Providence, Draconic Scale, Jotunn''s Revenge, Spectral Armor,
    Pharaoh''s Curse, Shield Splitter, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, The Crusher, Midgardian Mail, Eye of the Storm, Hydra''s Lament,
    Shogun''s Ofuda, Helm of Radiance, Magi''s Cloak, Runeforged Hammer, Gladiator''s
    Shield, Screeching Gargoyle, Ancile, Prophetic Cloak, Xibalban Effigy, Void Shield,
    Hide of the Nemean Lion, Doublet of Binding, Rod of Asclepius, Yogi''s Necklace,
    Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.55
      pick: 0.25
      fit: 0.38
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.38
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.12
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.67
  starter: *id001
---
