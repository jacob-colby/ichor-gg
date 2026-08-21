---
type: smite-build
god: Hou Yi
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Mark
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.62
  slot_order:
  - name: Tyrfing
    pick_rate: 0.55
    win_rate: 0.57
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.21
      win_rate: 0.51
    - name: Avenging Blade
      pick_rate: 0.09
      win_rate: 0.52
  - name: Odysseus' Bow
    pick_rate: 0.31
    win_rate: 0.56
    alternates:
    - name: Dagger of Frenzy
      pick_rate: 0.28
      win_rate: 0.53
    - name: Toxic Blade
      pick_rate: 0.1
      win_rate: 0.52
  - name: Silverbranch Bow
    pick_rate: 0.14
    win_rate: 0.53
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.18
      win_rate: 0.53
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.58
  - name: The Executioner
    pick_rate: 0.17
    win_rate: 0.47
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.22
      win_rate: 0.54
    - name: Riptalon
      pick_rate: 0.11
      win_rate: 0.51
  - name: Riptalon
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.15
      win_rate: 0.56
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.52
  - name: Manchu Bow
    pick_rate: 0.1
    win_rate: 0.56
    alternates:
    - name: Riptalon
      pick_rate: 0.09
      win_rate: 0.55
    - name: Dominance
      pick_rate: 0.08
      win_rate: 0.71
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.33
    win_rate: 0.58
  - name: Hunter's Cowl
    pick_rate: 0.25
    win_rate: 0.61
  - name: Gilded Arrow
    pick_rate: 0.15
    win_rate: 0.37
  source_url: https://smitebrain.com/gods/hou-yi/
  last_verified: '2026-08-21'
  god_win_rate: 0.5339366515837104
  god_matches_won: 944
  god_matches_played: 1768
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Berserker''s
    Shield, Golden Blade, Lernaean Bow, Gluttonous Grimoire, Soul Gem, The Crusher,
    Bragi''s Harp, Tekko-Kagi, Deathbringer, Damaru, The Reaper, Runeforged Hammer,
    Hydra''s Lament, Genji''s Guard, Demon Blade, Breastplate of Valor, Pharaoh''s
    Curse, Amanita Charm, Bracer of The Abyss, Kinetic Cuirass, Spear of the Magus,
    Heartseeker, Musashi''s Dual Swords, Shogun''s Ofuda, Toxic Blade, Spear of Desolation,
    Obsidian Shard, Freya''s Tears, Shield Splitter, Helm of Radiance, Eye of Providence,
    Qin''s Blade, Avenging Blade, Titan''s Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.25
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.62
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.47
    Dominance:
      total: 0.57
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.52
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.5
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Berserker''s Shield, The Crusher, Spear of Desolation, Spear of the Magus, Hydra''s
    Lament, Genji''s Guard, Breastplate of Valor, Obsidian Shard, Lernaean Bow, Bragi''s
    Harp, Heartseeker, The Reaper, Golden Blade, Runeforged Hammer, Ancient Signet,
    Tekko-Kagi, Doom Orb, Helm of Radiance, The World Stone, Bracer of The Abyss,
    Amanita Charm, Chronos'' Pendant, Freya''s Tears, Kinetic Cuirass, The Cosmic
    Horror, Ethereal Staff, Deathbringer, Damaru, Rod of Asclepius, Bancroft''s Talon,
    Wish-Granting Pearl, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.48
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.48
    Dominance:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.48
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.38
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  - Damaru
  - Deathbringer
  flex_slots:
  - Deathbringer
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Jotunn''s Revenge, Nimble Ring, Berserker''s
    Shield, Golden Blade, Lernaean Bow, Gluttonous Grimoire, Soul Gem, The Crusher,
    Deathbringer, Damaru, The Reaper, Bragi''s Harp, Runeforged Hammer, Tekko-Kagi,
    Genji''s Guard, Demon Blade, Breastplate of Valor, Hydra''s Lament, Amanita Charm,
    Musashi''s Dual Swords, Pharaoh''s Curse, Kinetic Cuirass, Spear of the Magus,
    Bracer of The Abyss, Heartseeker, Shogun''s Ofuda, Spear of Desolation, Toxic
    Blade, Obsidian Shard, Freya''s Tears, Helm of Radiance, Shield Splitter, Eye
    of Providence, Rage, Avenging Blade, Titan''s Bane.'
  slot_scores:
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.58
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.49
    Dominance:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.49
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.47
    Damaru:
      total: 0.48
      efficiency: 0.5
      win: 0.53
      pick: 0.0
      fit: 0.44
    Deathbringer:
      total: 0.48
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Dominance
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, Jotunn''s Revenge, Ethereal Staff, Rod of Asclepius,
    The Reaper, Nimble Ring, Gluttonous Grimoire, Death Metal, Pharaoh''s Curse, Golden
    Blade, Freya''s Tears, Genji''s Guard, Runeforged Hammer, Breastplate of Valor,
    Blood-Bound Book, Shogun''s Ofuda, Yogi''s Necklace, Phoenix Feather, Shifter''s
    Shield, Chandra''s Grace, Shield Splitter, Bancroft''s Talon, Lernaean Bow, Mantle
    Of Discord, Stone of Binding, The Crusher, Spectral Armor, Eye of the Storm, Erosion,
    Lifebinder, Helm of Radiance, Leviathan''s Hide, Eye of Providence, Daybreak Gavel,
    Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.44
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.38
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Silverbranch Bow
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem,
    The Crusher, Nimble Ring, Berserker''s Shield, Death Metal, The Reaper, Tekko-Kagi,
    Spear of the Magus, Heartseeker, Obsidian Shard, Spear of Desolation, Avenging
    Blade, Stone of Binding, Toxic Blade, Lernaean Bow, Screeching Gargoyle, Titan''s
    Bane, Golden Blade, Doom Orb, Genji''s Guard, The Cosmic Horror, Breastplate of
    Valor, Runeforged Hammer, The World Stone, Amanita Charm, Hydra''s Lament, Dreamer''s
    Idol, Kinetic Cuirass, Void Shield, Deathbringer, Damaru, Bragi''s Harp, Pharaoh''s
    Curse, Avatar''s Parashu, Void Stone, Freya''s Tears.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.44
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.49
    Dominance:
      total: 0.55
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.41
    Riptalon:
      total: 0.56
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.63
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.53
      win: 0.53
      pick: 0.22
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  flex_slots:
  - Berserker's Shield
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Jotunn''s Revenge, Berserker''s Shield,
    Death Metal, Golden Blade, Lernaean Bow, Gluttonous Grimoire, Soul Gem, The Crusher,
    Bragi''s Harp, Tekko-Kagi, Toxic Blade, Genji''s Guard, Runeforged Hammer, Breastplate
    of Valor, The Reaper, Pharaoh''s Curse, Deathbringer, Damaru, Hydra''s Lament,
    Amanita Charm, Bracer of The Abyss, Demon Blade, Kinetic Cuirass, Qin''s Blade,
    Shogun''s Ofuda, Spear of the Magus, Heartseeker, Freya''s Tears, Obsidian Shard,
    Spear of Desolation, Musashi''s Dual Swords, Eye of Providence, Helm of Radiance,
    Shield Splitter, Avenging Blade, Ancient Signet.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.21
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.67
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.41
    Dominance:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.5
    Riptalon:
      total: 0.55
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Tyrfing
  - Dominance
  - Soul Gem
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Nimble Ring, Genji''s Guard, Breastplate of Valor, Death Metal, Berserker''s
    Shield, Spear of Desolation, Hydra''s Lament, Freya''s Tears, Gluttonous Grimoire,
    Chronos'' Pendant, Shield of the Phoenix, Lernaean Bow, Screeching Gargoyle, Golden
    Blade, The Crusher, Arondight, Gem of Focus, Amanita Charm, Spear of the Magus,
    Kinetic Cuirass, Runeforged Hammer, Bragi''s Harp, Totem of Death, Obsidian Shard,
    Bracer of The Abyss, Helm of Radiance, Pharaoh''s Curse, The Reaper, Deathbringer,
    Damaru, Tekko-Kagi, Eye of Providence, Chandra''s Grace, Ancient Signet, Shogun''s
    Ofuda, Ethereal Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.28
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.28
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.4
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.44
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.37
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Dominance
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble
    Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Spear of Desolation, Berserker''s
    Shield, Spear of the Magus, Obsidian Shard, The Crusher, Genji''s Guard, Breastplate
    of Valor, Bragi''s Harp, Helm of Radiance, Lernaean Bow, Hydra''s Lament, The
    Reaper, Bracer of The Abyss, Chronos'' Pendant, Doom Orb, Golden Blade, The Cosmic
    Horror, Tekko-Kagi, Ancient Signet, Freya''s Tears, The World Stone, Heartseeker,
    Runeforged Hammer, Amanita Charm, Ethereal Staff, Rod of Asclepius, Blood-Bound
    Book, Kinetic Cuirass, Dreamer''s Idol, Gem of Focus, Deathbringer, Jade Scepter,
    Damaru.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.34
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.11
    Dominance:
      total: 0.54
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.38
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.43
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Dominance
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Death Metal, Nimble Ring, Gluttonous Grimoire, Soul Gem, Berserker''s Shield,
    The Crusher, Spear of the Magus, Obsidian Shard, Spear of Desolation, The Reaper,
    Lernaean Bow, Bragi''s Harp, Golden Blade, Tekko-Kagi, Heartseeker, Runeforged
    Hammer, Bracer of The Abyss, Hydra''s Lament, Genji''s Guard, Helm of Radiance,
    Breastplate of Valor, Doom Orb, The Cosmic Horror, Amanita Charm, Deathbringer,
    Damaru, The World Stone, Ancient Signet, Titan''s Bane, Kinetic Cuirass, Ethereal
    Staff, Rod of Asclepius, Blood-Bound Book, Dreamer''s Idol, Toxic Blade, Chronos''
    Pendant.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.33
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.52
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.51
    Dominance:
      total: 0.56
      efficiency: 0.45
      win: 0.71
      pick: 0.25
      fit: 0.45
    Riptalon:
      total: 0.53
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.46
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death
    Metal, Berserker''s Shield, Golden Blade, Lernaean Bow, Gluttonous Grimoire, Soul
    Gem, The Crusher, Bragi''s Harp, Tekko-Kagi, Deathbringer, Damaru, The Reaper,
    Runeforged Hammer, Hydra''s Lament, Genji''s Guard, Demon Blade, Breastplate of
    Valor, Pharaoh''s Curse, Amanita Charm, Bracer of The Abyss, Kinetic Cuirass,
    Spear of the Magus, Heartseeker, Musashi''s Dual Swords, Shogun''s Ofuda, Toxic
    Blade, Spear of Desolation, Obsidian Shard, Freya''s Tears, Shield Splitter, Helm
    of Radiance, Eye of Providence, Qin''s Blade, Avenging Blade, Titan''s Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.25
    Tyrfing:
      total: 0.55
      efficiency: 0.48
      win: 0.57
      pick: 0.55
      fit: 0.62
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.4
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.47
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.1
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Berserker's Shield
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Nimble Ring, Death Metal, Berserker''s Shield, Golden Blade, Lernaean Bow, Gluttonous
    Grimoire, Soul Gem, The Crusher, Bragi''s Harp, Tekko-Kagi, Deathbringer, Damaru,
    The Reaper, Runeforged Hammer, Hydra''s Lament, Genji''s Guard, Demon Blade, Breastplate
    of Valor, Pharaoh''s Curse, Amanita Charm, Bracer of The Abyss, Kinetic Cuirass,
    Spear of the Magus, Heartseeker, Musashi''s Dual Swords, Shogun''s Ofuda, Toxic
    Blade, Spear of Desolation, Obsidian Shard, Freya''s Tears, Shield Splitter, Helm
    of Radiance, Eye of Providence, Qin''s Blade, Avenging Blade, Titan''s Bane.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.4
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.53
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.59
      pick: 0.37
      fit: 0.5
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.1
  swaps:
  - added: Riptalon
    removed: Tyrfing
    reason: community 59% win over 301 matches (vs 53% on this god), taking the model's
      weakest slot from Tyrfing
  starter: *id001
---
