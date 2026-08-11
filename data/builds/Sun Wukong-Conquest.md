---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.39
    win_rate: 0.54
    alternates:
    - name: Mystical Mail
      pick_rate: 0.08
      win_rate: 0.64
    - name: Runeforged Hammer
      pick_rate: 0.06
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.52
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.58
  - name: Gladiator's Shield
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.61
  - name: Sundering Echo
    pick_rate: 0.13
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.51
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.56
  - name: Draconic Scale
    pick_rate: 0.09
    win_rate: 0.59
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.65
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.48
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.48
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.4
    - name: Shell of Rebuke
      pick_rate: 0.03
      win_rate: 0.58
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.44
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.29
    win_rate: 0.49
  - name: Archmage's Gem
    pick_rate: 0.09
    win_rate: 0.51
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-10'
  god_win_rate: 0.5430016863406408
  god_matches_won: 322
  god_matches_played: 593
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
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Breastplate
    of Valor, Amanita Charm, Jotunn''s Revenge, The Crusher, Golden Blade, Runeforged
    Hammer, Oni Hunter''s Garb, Pharaoh''s Curse, Eye of the Storm, Hydra''s Lament,
    Lernaean Bow, Shield Splitter, Shield of the Phoenix, Spectral Armor, Avenging
    Blade, Shogun''s Ofuda, Death Metal, Erosion, Soul Gem, Eye of Providence, Damaru,
    Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail, Rod of Asclepius, Bragi''s
    Harp, Dominance, Triton''s Conch, Tyrfing, Jade Scepter, Helm of Radiance, The
    Reaper, Wyrmskin Hide, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.11
      fit: 0.17
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.42
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Breastplate of Valor, Gluttonous Grimoire, Soul Gem, Rod of Asclepius, The Crusher,
    Jotunn''s Revenge, Oni Hunter''s Garb, Pharaoh''s Curse, Runeforged Hammer, Golden
    Blade, The Reaper, Eye of the Storm, Chandra''s Grace, Riptalon, Shield Splitter,
    Erosion, Phoenix Feather, Spectral Armor, Eye of Providence, Blood-Bound Book,
    Hydra''s Lament, Shogun''s Ofuda, Bancroft''s Talon, Lernaean Bow, Leviathan''s
    Hide, Avenging Blade, Lifebinder, Midgardian Mail, Death Metal, Yogi''s Necklace,
    Damaru, Freya''s Tears, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.11
      fit: 0.2
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.71
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.59
      pick: 0.19
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Berserker''s
    Shield, Soul Gem, Breastplate of Valor, Avenging Blade, Kinetic Cuirass, Spear
    of the Magus, Amanita Charm, The Cosmic Horror, Riptalon, The Reaper, Void Shield,
    Silverbranch Bow, Stone of Binding, Runeforged Hammer, Oni Hunter''s Garb, Heartseeker,
    Golden Blade, Hydra''s Lament, Screeching Gargoyle, Tekko-Kagi, Obsidian Shard,
    Pharaoh''s Curse, Void Stone, Spear of Desolation, Lernaean Bow, Eye of the Storm,
    Titan''s Bane, Spectral Armor, Shield of the Phoenix, Death Metal, Shield Splitter,
    Toxic Blade, Shogun''s Ofuda, Damaru, The World Stone, Freya''s Tears.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.48
      win: 0.55
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.61
      pick: 0.11
      fit: 0.12
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Gluttonous Grimoire
  - Riptalon
  flex_slots:
  - Riptalon
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Gluttonous Grimoire, Golden Blade, Breastplate
    of Valor, Riptalon, Pharaoh''s Curse, Kinetic Cuirass, Amanita Charm, The Crusher,
    Jotunn''s Revenge, Lernaean Bow, Silverbranch Bow, Tyrfing, Shogun''s Ofuda, Oni
    Hunter''s Garb, Soul Gem, Runeforged Hammer, Hydra''s Lament, Bracer of The Abyss,
    Spectral Armor, Shield of the Phoenix, Eros'' Bow, Toxic Blade, Dominance, Bragi''s
    Harp, Death Metal, Yogi''s Necklace, Eye of the Storm, Erosion, Nimble Ring, Shield
    Splitter, Rod of Asclepius, Leviathan''s Hide, Spear of the Magus, Damaru, Blood-Bound
    Book, Eye of Providence, Freya''s Tears.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.11
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.61
      pick: 0.11
      fit: 0.11
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Jotunn''s Revenge,
    Soul Gem, Gluttonous Grimoire, Berserker''s Shield, Hydra''s Lament, Shield of
    the Phoenix, Kinetic Cuirass, Amanita Charm, Chronos'' Pendant, Freya''s Tears,
    Spear of Desolation, The Crusher, Chandra''s Grace, Oni Hunter''s Garb, Screeching
    Gargoyle, Pharaoh''s Curse, Gem of Focus, Runeforged Hammer, Golden Blade, Spectral
    Armor, Rod of Asclepius, Arondight, Death Metal, Spear of the Magus, Lernaean
    Bow, Helm of Radiance, Jade Scepter, Shogun''s Ofuda, Gladiator''s Shield, Erosion,
    Yogi''s Necklace, Prophetic Cloak, The Cosmic Horror, Eye of the Storm, Bracer
    of The Abyss, Leviathan''s Hide, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.53
      pick: 0.25
      fit: 0.44
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.66
      win: 0.61
      pick: 0.11
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.53
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.55
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass,
    Amanita Charm, Jotunn''s Revenge, The Crusher, Golden Blade, Runeforged Hammer,
    Oni Hunter''s Garb, Pharaoh''s Curse, Eye of the Storm, Hydra''s Lament, Lernaean
    Bow, Shield Splitter, Breastplate of Valor, Shield of the Phoenix, Spectral Armor,
    Avenging Blade, Shogun''s Ofuda, Death Metal, Freya''s Tears, Erosion, Soul Gem,
    Eye of Providence, Damaru, Leviathan''s Hide, Yogi''s Necklace, Midgardian Mail,
    Rod of Asclepius, Bragi''s Harp, Dominance, Triton''s Conch, Tyrfing, Jade Scepter,
    Helm of Radiance, The Reaper, Wyrmskin Hide.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.55
      pick: 0.0
      fit: 0.55
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.42
  starter: *id001
---
